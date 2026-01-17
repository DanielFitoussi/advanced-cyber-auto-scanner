import sys
from tools.zap_runner import run_zap_scan
from tools.nuclei_runner import run_nuclei_scan
from tools.idor_check import run_idor_check
from tools.semgrep_runner import run_semgrep_scan


def main():
    if len(sys.argv) < 2:
        print("usage: python scanner.py <target_url>")
        return

    target_url = sys.argv[1]
    target_path = "."

    run_zap_scan(target_url)
    run_nuclei_scan(target_url)
    run_semgrep_scan(target_path)
    run_idor_check()


if __name__ == "__main__":
    main()
