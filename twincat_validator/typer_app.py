"""MCP application instance and shared server state.

This module creates the FastMCP instance and initializes all shared objects
(config, validation engine, fix engine) that tool and resource modules import.

Import order:
    typer_configuration  ← no dependencies on other mcp_* modules
    typer_responses  ← no dependencies on other mcp_* modules
    mcp_tools_*  ← depend on typer_configuration and typer_responses
    mcp_resources  ← depend on typer_configuration
    server  ← facade, imports all of the above
"""

import typer

from twincat_validator.typer_tools_validation import app as validation_app
from twincat_validator.typer_tools_fix import app as fix_app
from twincat_validator.typer_tools_batch import app as batch_app
from twincat_validator.typer_tools_orchestration import app as orchestration_app
# ============================================================================
# TYPER INSTANCE
# ============================================================================

app = typer.Typer()

app.add_typer(validation_app, name="validate")
app.add_typer(fix_app, name="fix")
# app.add_typer(batch_app)
# app.add_typer(orchestration_app)
