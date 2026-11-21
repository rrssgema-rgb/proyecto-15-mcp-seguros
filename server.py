"""
Servidor MCP de consulta de coberturas de seguros.
Proyecto 15 - Master AI Engineer.
"""

import logging
import re
import sys

from mcp.server.mcpserver import MCPServer

# Los logs deben salir por stderr, nunca por stdout.
logging.basicConfig(
    stream=sys.stderr,
    level=logging.INFO,
    format="[mcp-seguros] %(levelname)s %(message)s"
)

log = logging.getLogger("mcp-seguros")

# Inicializar servidor MCP
mcp = MCPServer("mcp-seguros")


# Datos ficticios para las pruebas
POLIZAS = {
    "AUTO-1001": {
        "producto": "Seguro de automóvil",
        "coberturas": [
            "Responsabilidad civil",
            "Rotura de lunas",
            "Asistencia en carretera"
        ],
        "franquicia": "Sin franquicia"
    },
    "AUTO-1002": {
        "producto": "Seguro de automóvil",
        "coberturas": [
            "Responsabilidad civil",
            "Robo",
            "Incendio"
        ],
        "franquicia": "Franquicia de 300 euros"
    }
}


@mcp.tool()
def consultar_cobertura(numero_poliza: str) -> str:
    """
    Consulta las coberturas de una póliza de automóvil.

    Utiliza el número de póliza para recuperar el producto,
    las coberturas contratadas y la franquicia.

    Args:
        numero_poliza: Identificador de la póliza.
        Formato esperado: AUTO-XXXX, por ejemplo AUTO-1001.
    """

    numero_poliza = numero_poliza.strip().upper()

    # Validar formato de entrada
    if not re.fullmatch(r"AUTO-\d{4}", numero_poliza):
        log.warning("Formato de póliza no válido: %s", numero_poliza)
        return (
            "Error: formato de póliza no válido. "
            "Utiliza AUTO-XXXX, por ejemplo AUTO-1001."
        )

    # Comprobar existencia de la póliza
    poliza = POLIZAS.get(numero_poliza)

    if poliza is None:
        log.warning("Póliza no encontrada: %s", numero_poliza)
        return f"No se ha encontrado la póliza {numero_poliza}."

    log.info("Consulta realizada para la póliza %s", numero_poliza)

    coberturas = "\n".join(
        f"- {cobertura}" for cobertura in poliza["coberturas"]
    )

    return (
        f"Póliza: {numero_poliza}\n"
        f"Producto: {poliza['producto']}\n"
        f"Coberturas:\n{coberturas}\n"
        f"Franquicia: {poliza['franquicia']}"
    )


if __name__ == "__main__":
    log.info("Iniciando servidor MCP por STDIO...")
    mcp.run()
