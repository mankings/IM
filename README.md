# IM

## How to run
powershell
```
cd mmiframkeworkV2
start.bat
```

powershell
```
cd FusionEngine
start.bat
```

anaconda prompt
```
conda activate rasa-env
cd rasaDemo
rasa train			# if needed
rasa run --enable-api -m .\models\ --cors "*"
```

powershell
```
cd WebAppAssistantV2
start_web_app.bat
```