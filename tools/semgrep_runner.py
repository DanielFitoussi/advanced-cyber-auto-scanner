import subprocess
import os


def run_semgrep_scan(target_path):
    print("[*] Running Semgrep static analysis on:", target_path)

    output_file = "semgrep_report.json"

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"

    try:
        subprocess.run(
            [
                "semgrep",
                "--config=auto",
                "--json",
                "--output",
                output_file,
                target_path
            ],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False
        )

        if not os.path.exists(output_file):
            print("[!] Semgrep failed to generate report (encoding issue or no findings)")
            return False

        return True

    except FileNotFoundError:
        print("[!] Semgrep is not installed or not in PATH")
        return False
