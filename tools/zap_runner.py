import subprocess
import os

ZAP_DIR = r"C:\Program Files\ZAP\Zed Attack Proxy"
ZAP_PATH = r"C:\Program Files\ZAP\Zed Attack Proxy\zap.bat"

def run_zap_scan(target_url):
    if not target_url:
        print("[!] ZAP skipped (no target_url provided)")
        return

    if not os.path.exists(ZAP_PATH):
        print("[!] ZAP not found at:", ZAP_PATH)
        return

    print("[*] Running OWASP ZAP baseline scan on:", target_url)

    output_file = os.path.join(os.getcwd(), "zap_report.json")

    command = [
        ZAP_PATH,
        "-cmd",
        "-quickurl", target_url,
        "-quickprogress",
        "-quickout", output_file,
        
    ]

    try:
        subprocess.run(
            command,
            cwd=ZAP_DIR,
            check=True
        )
        print("[+] ZAP scan finished. Report: zap_report.json")
    except Exception as e:
        print("[!] ZAP scan failed:", e)
