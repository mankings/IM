# IM

## How to run

### Iniciar MMI
powershell
```
cd mmiframkeworkV2
start.bat
```

### Iniciar Fusion
powershell
```
cd FusionEngine
start.bat
```

### Iniciar Rasa
anaconda prompt
```
conda activate rasa-env
cd rasaDemo
rasa train			# if needed
rasa run --enable-api -m .\models\ --cors "*"
```

### Iniciar RestAPI
anaconda prompt
```
conda create --name im-env python=3.8		# if needed
conda activate im-env
uvicorn interaction-manager:app --port 5000
```

### Iniciar AppGUI 
powershell
```
cd WebAppAssistantV2
start_web_app.bat
```
--- 
## Testar a implementação
Pode iniciar manualmente o emulador, arrastando na pasta interaction_manager/pokemon o ficheiro leaf-green.gba para o visualboyadvance-m.exe, ou através do controlo por voz, seguindo um dos seguintes exemplos do intent launch_game.

**NOTA**: Para ambos os casos quando o jogo inicia deve pressionar a tecla F2 para entrar no jogo guardado e, assim, evitar o tutorial e configurações iniciais.

