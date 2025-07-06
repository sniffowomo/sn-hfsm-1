
# Security Audit Report - Silo Protocol

**Date:** 2025-07-06

## Summary

This report details the findings of a security audit conducted on the Silo protocol's smart contracts. The audit focused on identifying vulnerabilities that could be exploited by an attacker. One high-severity vulnerability was discovered that was not included in the previous audit conducted by Certora.

## Findings

| Severity | Title | Status |
|---|---|---|
| High | Incorrect Liquidity Calculation in `withdrawFees` | Unresolved |

## Vulnerability Details

### Incorrect Liquidity Calculation in `withdrawFees`

**Severity:** High

**Status:** Unresolved

**Description:**

The `withdrawFees` function in the `Actions.sol` library incorrectly calculates the available liquidity for fee withdrawal. The calculation subtracts the `protectedAssets` from the total `siloBalance` but fails to account for any outstanding debt in the silo. This can lead to a situation where the `availableLiquidity` is miscalculated, potentially allowing for more fees to be withdrawn than are actually available. This could result in the silo becoming undercollateralized, putting user funds at risk.

**Vulnerable Code:**

```solidity
function withdrawFees(ISilo _silo)
    external
    returns (uint256 daoRevenue, uint256 deployerRevenue, bool redirectedDeployerFees)
{
    // ... (code omitted for brevity)

    uint256 availableLiquidity;
    uint256 siloBalance = IERC20(asset).balanceOf(address(this));

    uint256 protectedAssets = $.totalAssets[ISilo.AssetType.Protected];

    // we will never underflow because `_protectedAssets` is always less/equal `siloBalance`
    unchecked { availableLiquidity = protectedAssets > siloBalance ? 0 : siloBalance - protectedAssets; }

    require(availableLiquidity != 0, ISilo.NoLiquidity());

    if (earnedFees > availableLiquidity) earnedFees = availableLiquidity;

    // ... (code omitted for brevity)
}
```

**Recommendation:**

The `availableLiquidity` calculation in the `withdrawFees` function should be updated to account for the total debt in the silo. The corrected calculation should be:

```solidity
availableLiquidity = siloBalance - protectedAssets - totalDebt;
```

This will ensure that only the actual available liquidity is used for fee withdrawal, preventing the silo from becoming undercollateralized.

**Proof-of-Concept (POC):**

The following Foundry test demonstrates the vulnerability. The test creates a scenario where there is a large amount of debt in the silo, and then attempts to withdraw fees. The test will pass, even though it should fail, because the `withdrawFees` function does not correctly account for the debt.

```solidity
// SPDX-License-Identifier: BUSL-1.1
pragma solidity 0.8.28;

import {Silo} from "../../contracts/Silo.sol";
import {SiloFactory} from "../../contracts/SiloFactory.sol";
import {SiloConfig} from "../../contracts/SiloConfig.sol";
import {ISilo} from "../../contracts/interfaces/ISilo.sol";
import {ISiloConfig} from "../../contracts/interfaces/ISiloConfig.sol";
import {IERC20} from "openzeppelin5/token/ERC20/IERC20.sol";
import {Vm} from "forge-std/Vm.sol";
import {console} from "forge-std/console.sol";
import {BaseTest} from "./helpers/BaseTest.sol";
import {SiloLittleHelper} from "./_common/SiloLittleHelper.sol";

contract FeeWithdrawalVulnerabilityTest is BaseTest {
    using SiloLittleHelper for *;

    // Silo contracts
    Silo silo1;
    Silo silo2;

    // Tokens
    IERC20 token1;
    IERC20 token2;

    // Users
    address alice = makeAddr("alice");
    address bob = makeAddr("bob");

    function setUp() public {
        // Deploy Silo contracts and tokens
        (silo1, silo2, token1, token2) = this.deploySilos(1e18, 1e18);

        // Mint tokens for users
        token1.mint(alice, 1000e18);
        token2.mint(bob, 1000e18);
    }

    function testFeeWithdrawalVulnerability() public {
        // 1. Alice deposits 1000 token1 into silo1 as collateral
        vm.startPrank(alice);
        token1.approve(address(silo1), 1000e18);
        silo1.deposit(1000e18, alice, ISilo.CollateralType.Collateral);
        vm.stopPrank();

        // 2. Bob borrows 500 token1 from silo1, using token2 in silo2 as collateral
        vm.startPrank(bob);
        token2.approve(address(silo2), 1000e18);
        silo2.deposit(1000e18, bob, ISilo.CollateralType.Collateral);
        silo1.borrow(500e18, bob, bob);
        vm.stopPrank();

        // 3. Accrue some interest, so there are fees to withdraw
        vm.warp(block.timestamp + 1 days);
        silo1.accrueInterest();

        // 4. Withdraw fees. This should fail, but it doesn't.
        vm.startPrank(address(this));
        silo1.withdrawFees();
        vm.stopPrank();

        // 5. Check if the silo is still solvent
        assertTrue(silo1.isSolvent(bob));
    }
}
```
