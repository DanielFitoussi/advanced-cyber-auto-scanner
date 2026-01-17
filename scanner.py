from tools.zap_runner import run_zap_scan


def main():
    target_url = "http://localhost:3000"
    run_zap_scan(target_url)


if __name__ == "__main__":
    main()
