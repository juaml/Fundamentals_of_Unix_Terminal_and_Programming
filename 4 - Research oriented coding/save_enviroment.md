## Save the enviroment

1. Save your enviroment in a .txt file

```bash
#!/bin/bash

python -m venv env && source env/bin/activate

pip freeze > requirements.txt

```

1. Save your enviroment in a .yml file (For Conda)

```bash
#!/bin/bash

conda env export > environment.yml

```
