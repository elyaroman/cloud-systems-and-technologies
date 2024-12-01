import argparse

def main():
    parser = argparse.ArgumentParser(description="Простое приложение для работы с API ключом")
    parser.add_argument('--api-key', required=True, help="API ключ для доступа")
    args = parser.parse_args()



if __name__ == "__main__":
    main()
