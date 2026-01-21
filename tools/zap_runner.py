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

    command = [
        ZAP_PATH,
        "-cmd",
        "-quickurl", target_url,
        "-quickprogress",
        "-quickout", os.path.join(os.getcwd(), "zap_report.html")

    ]

    try:
        subprocess.run(
            command,
            cwd=ZAP_DIR,   # ⭐ זה השינוי הקריטי ⭐
            check=True
        )
        print("[+] ZAP scan finished. Report: zap_report.html")
    except Exception as e:
        print("[!] ZAP scan failed:", e)
