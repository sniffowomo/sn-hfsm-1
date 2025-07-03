#!/bin/bash

# Development server startup script with timeout handling
# This addresses the issue mentioned in AGENTS.MD about bun run dev getting stuck

echo "Starting development server..."

# Try to start the dev server with a timeout
timeout 15s bun run dev &
DEV_PID=$!

# Wait a bit to see if it starts successfully
sleep 3

# Check if the process is still running
if kill -0 $DEV_PID 2>/dev/null; then
    echo "✅ Development server started successfully!"
    echo "🌐 Visit: http://localhost:5173"
    echo "Press Ctrl+C to stop the server"
    wait $DEV_PID
else
    echo "⚠️  Dev server startup timed out or failed"
    echo "🔄 Trying alternative approach..."
    
    # Alternative: try with different port or clean start
    echo "Cleaning node modules and trying again..."
    bun install --force
    timeout 15s bun run dev --port 5174 &
    ALT_PID=$!
    
    sleep 3
    if kill -0 $ALT_PID 2>/dev/null; then
        echo "✅ Development server started on alternative port!"
        echo "🌐 Visit: http://localhost:5174"
        wait $ALT_PID
    else
        echo "❌ Unable to start development server"
        echo "💡 Try running 'bun run build' to test the production build"
    fi
fi