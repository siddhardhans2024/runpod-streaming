import runpod
import time


def async_generator_handler(job):
    input = job["input"]
    count = input["n"]
    for i in range(count):
        # Generate an asynchronous output token
        output = f"Generated async token output {i}"
        yield output

        # Simulate an asynchronous task, such as processing time for a large language model
        time.sleep(1)


# Configure and start the RunPod serverless function
runpod.serverless.start(
    {
        "handler": async_generator_handler,  # Required: Specify the async handler
        "return_aggregate_stream": True,  # Optional: Aggregate results are accessible via /run endpoint
    }
)
