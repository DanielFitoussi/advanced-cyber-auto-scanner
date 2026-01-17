from tools.zap_runner import run_zap_scan
from tools.idor_check import run_idor_check


def main():
    target_url = "http://localhost:3000"

    run_zap_scan(target_url)
    run_idor_check()


if __name__ == "__main__":
    main()
