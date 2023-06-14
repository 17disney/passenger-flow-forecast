/usr/bin/python3 -m pip freeze>modules.txt
/opt/homebrew/bin/python3.9 -m pip uninstall -r modules.txt -y

/usr/bin/python3 -m pip install seaborn matplotlib pandas tensorflow-macos tensorflow_hub jax scipy jaxlib etils
/usr/bin/python3 -m pip install tensorflowjs==4.1.0 --no-deps
/usr/bin/python3 -m pip install tensorflowjs==3.1.0 --no-deps

/usr/bin/python3 -m pip install matplotlib_inline

/usr/bin/python3 -m pip install fbprophet




/opt/homebrew/bin/python3.8 -m pip install sktime
/usr/bin/python3 -m pip install sktime

/opt/homebrew/bin/python3.8 -m pip uninstall holidays -y
/opt/homebrew/bin/python3.8 -m pip install holidays==0.23

/opt/homebrew/bin/python3.8-m pip install neuralprophet

/usr/local/bin/python3 -m pip install neuralprophet