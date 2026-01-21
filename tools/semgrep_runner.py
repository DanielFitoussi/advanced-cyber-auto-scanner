import subprocess

def run_semgrep_scan(target_path):
    print("[*] Running Semgrep static analysis on:", target_path)

    try:
        subprocess.run(
            [
                "semgrep",
                "--config=auto",
                target_path
            ],
            check=True
        )
    except FileNotFoundError:
        print("[!] Semgrep is not installed or not in PATH")
    except subprocess.CalledProcessError:
        print("[!] Semgrep scan failed")
