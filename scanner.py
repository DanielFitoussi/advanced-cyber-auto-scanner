import sys
from tools.zap_runner import run_zap_scan
from tools.idor_check import run_idor_check
from tools.nuclei_runner import run_nuclei_scan


def main():
    if len(sys.argv) < 2:
        print("usage: python scanner.py <target_url>")
        return

    target_url = sys.argv[1]

    run_zap_scan(target_url)
    run_nuclei_scan(target_url)
    run_idor_check()


if __name__ == "__main__":
    main()
