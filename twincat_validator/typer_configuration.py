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

from twincat_validator import ValidationEngine, FixEngine, TwinCATFile, CheckRegistry  # noqa: F401
from twincat_validator.config_loader import get_shared_config
from twincat_validator.exceptions import (  # noqa: F401
    UnsupportedFileTypeError,
    ConfigurationError,
    CheckNotFoundError,
)

# ============================================================================
# SHARED STATE
# ============================================================================

# Initialize configuration and engines at module level (singleton pattern)
config = get_shared_config()
validation_engine = ValidationEngine(config)
fix_engine = FixEngine(config)

# ============================================================================
# CONSTANTS
# ============================================================================

VALIDATION_CHECKS = config.validation_checks
FIX_CAPABILITIES = config.fix_capabilities
NAMING_CONVENTIONS = config.naming_conventions
SERVER_INFO = config.server_info
VALID_PROFILES = ("full", "llm_strict")
VALID_FORMAT_PROFILES = ("default", "twincat_canonical")
ERROR_SEVERITIES = ("error", "critical")
SUPPORTED_POU_SUBTYPES = ("function_block", "function", "program")
DEFAULT_ENFORCEMENT_MODE = "strict"
POLICY_RESPONSE_VERSION = "2"

# Best-effort in-memory loop guard state for orchestration hints.
_LOOP_GUARD_STATE: dict[str, dict[str, object]] = {}
