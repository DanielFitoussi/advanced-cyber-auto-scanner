import subprocess
import os


ZAP_AUTH_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2OTZiZGI0MTQ4ZDI3NTQxNTllY2ZiYTIiLCJ1c2VybmFtZSI6ImRhdmlkMTIzIiwiaWF0IjoxNzY5MTk1MzI4LCJleHAiOjE3NjkxOTg5Mjh9.oDTaBbV0h7kpwTgwCPo7aNy4l5Ar8c810Sdw-HBqeKQ"
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

    # 🔐 Authorization Header
    "-config", f"replacer.full_list(0).description=AuthHeader",
    "-config", f"replacer.full_list(0).enabled=true",
    "-config", f"replacer.full_list(0).matchtype=REQ_HEADER",
    "-config", f"replacer.full_list(0).matchstr=Authorization",
    "-config", f"replacer.full_list(0).regex=false",
    "-config", f"replacer.full_list(0).replacement=Bearer {ZAP_AUTH_TOKEN}",
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
