import { useForm } from "react-hook-form"

export default function Form1() {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm()

  const onSubmit = (data) => console.log(data)

  console.log(watch("example")) // Watch input value by name

  return (
    <div className="max-w-md w-full bg-gray-800 p-8 rounded-lg shadow-lg text-green-400">
      <h2 className="text-2xl font-bold mb-6 text-center">
        React Hook Form Example
      </h2>

      <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
        {/* Basic Input */}
        <div>
          <label className="block text-sm font-medium mb-2">
            Example Input
          </label>
          <input
            defaultValue="test"
            {...register("example")}
            className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        </div>

        {/* Required Input */}
        <div>
          <label className="block text-sm font-medium mb-2">
            Required Field
          </label>
          <input
            {...register("exampleRequired", { required: true })}
            className="w-full px-4 py-2 bg-gray-700 border border-gray-600 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-green-500"
          />
          {errors.exampleRequired && (
            <span className="text-red-400 text-sm mt-1 block">
              This field is required
            </span>
          )}
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          className="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-2 px-4 rounded-md transition-colors duration-200"
        >
          Submit
        </button>
      </form>
    </div>
  )
}
