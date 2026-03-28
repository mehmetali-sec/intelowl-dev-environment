import os
import subprocess

def check_docker_containers():
    print("--- Checking IntelOwl Microservices Status ---")
    try:
        # Docker servislerinin durumunu kontrol eden basit bir komut
        result = subprocess.run(['docker', 'compose', 'ps'], capture_output=True, text=True)
        if "uwsgi" in result.stdout and "redis" in result.stdout:
            print("[SUCCESS] Core services are visible in docker compose.")
        else:
            print("[WARNING] Some services might be down. Check 'docker compose ps'.")
    except Exception as e:
        print(f"[ERROR] Could not run docker command: {e}")

if __name__ == "__main__":
    check_docker_containers()
