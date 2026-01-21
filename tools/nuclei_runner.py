import subprocess

def run_nuclei_scan(target_url):
    if not target_url:
        print("[!] Nuclei skipped (no target_url provided)")
        return

    print("[*] Running Nuclei scan on:", target_url)

    try:
        subprocess.run(
            [
                "nuclei.exe",
                "-u", target_url,
                "-severity", "low,medium,high,critical",
                "-stats"
            ],
            check=True
        )
    except FileNotFoundError:
        print("[!] nuclei.exe not found in current directory")
    except subprocess.CalledProcessError:
        print("[!] Nuclei scan failed")
