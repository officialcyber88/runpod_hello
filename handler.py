import runpod

def handler(job):
    # job["input"] is whatever JSON you send from your app
    message = job["input"].get("message", "no message received")
    return {"reply": f"Hello, {message}!"}

runpod.serverless.start({"handler": handler})
