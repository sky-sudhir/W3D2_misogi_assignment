import subprocess

def run_ollama(model_name, prompt):
    result = subprocess.run(
        ['ollama', 'run', model_name],
        input=prompt.encode(),
        capture_output=True,
        timeout=180
    )
    return result.stdout.decode()
