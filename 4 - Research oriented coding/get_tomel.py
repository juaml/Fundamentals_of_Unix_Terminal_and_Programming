# %%
import sys
import subprocess
from pathlib import Path
from datetime import datetime


def get_python_version():
    """Get the current Python version in major.minor format"""
    return f"{sys.version_info.major}.{sys.version_info.minor}"


def get_installed_packages():
    """Get a list of installed packages and their versions using pip"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "freeze"],
            capture_output=True,
            text=True,
            check=True
        )
        packages = []
        for line in result.stdout.splitlines():
            if "==" in line:  # Only include packages with exact versions
                package, version = line.split("==")
                packages.append((package.strip(), version.strip()))
        return packages
    except subprocess.CalledProcessError as e:
        print(f"Error getting installed packages: {e}")
        return []


def generate_pyproject_toml(project_name="my_project", python_version=None,
                            packages=None):
    """Generate a pyproject.toml file content"""
    if python_version is None:
        python_version = get_python_version()
    if packages is None:
        packages = get_installed_packages()

    dependencies = [f'{pkg}=={ver}' for pkg, ver in packages if pkg.lower() != 'pip']       # noqa

    content = f"""# Generated pyproject.toml file
# Created: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
version = "0.1.0"
authors = [
    {{ name = "Your Name", email = "your.email@example.com" }},
]
description = "A short description of your project"
readme = "README.md"
requires-python = ">={python_version}"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = {dependencies}

[project.urls]
Homepage = "https://example.com"
Repository = "https://github.com/username/repository"
"""

    return content


def main():
    print("Generating pyproject.toml file...")

    # Get user input for project name
    project_name = input("Enter your project name (default: my_project): ") or "my_project"     # noqa

    # Generate the content
    content = generate_pyproject_toml(project_name)

    # Write to file
    file_path = Path("pyproject.toml")
    if file_path.exists():
        overwrite = input("pyproject.toml already exists. Overwrite? (y/n): ").lower()      # noqa
        if overwrite != 'y':
            print("Aborted.")
            return

    with open(file_path, "w") as f:
        f.write(content)

    print(f"Successfully created {file_path}")


if __name__ == "__main__":
    main()

# %%
