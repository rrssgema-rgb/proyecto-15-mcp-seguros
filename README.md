# Proyecto 15 - Servidor MCP de seguros

## Descripción

Servidor MCP desarrollado en Python para consultar las coberturas de pólizas de automóvil.

Utiliza el transporte STDIO y permite conectarse a Claude Code.

## Herramienta disponible

### consultar_cobertura

Consulta las coberturas contratadas de una póliza de automóvil.

**Parámetro:**
- `numero_poliza`: identificador con formato AUTO-XXXX.

**Información devuelta:**
- Producto.
- Coberturas.
- Franquicia.

El servidor valida el formato de entrada y controla las pólizas inexistentes.

## Tecnologías

- Python 3.14
- MCP SDK
- uv
- Claude Code
- Transporte STDIO

## Instalación

Desde la carpeta del proyecto:

```powershell
python -m pip install uv
python -m uv sync
```

## Ejecución

```powershell
python -m uv run python server.py
```

El servidor utiliza STDIO y registra los mensajes de diagnóstico en stderr.

## Conexión con Claude Code

El archivo `.mcp.json` contiene la configuración del servidor MCP para el proyecto.

Para registrar el servidor manualmente:

```powershell
claude mcp add --scope project mcp-seguros -- python -m uv run python server.py
```

## Pruebas realizadas

| Caso | Resultado |
|---|---|
| Consulta de AUTO-1001 | Correcto |
| Formato incorrecto AUTO-12A4 | Error controlado |
| Póliza inexistente AUTO-9999 | Error controlado |

## Evidencias

La carpeta `evidencias/` contiene la captura de Claude Code utilizando la herramienta MCP.

## Datos de prueba

Las pólizas utilizadas son ficticias y están definidas en `server.py`.