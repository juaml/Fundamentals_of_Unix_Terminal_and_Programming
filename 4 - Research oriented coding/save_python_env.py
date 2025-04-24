# %%
import subprocess


def save_python_environment(output_file="environment.yml"):
    try:
        with open(output_file, "w") as f:
            subprocess.run(["conda", "env", "export"], stdout=f, check=True)
        print(f"Environment saved to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    save_python_environment()