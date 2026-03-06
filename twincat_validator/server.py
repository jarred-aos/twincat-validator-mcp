#!/usr/bin/env python3
"""
TwinCAT Validator MCP Server — thin facade.

The real implementation lives in the sub-modules:
- typer_configuration.py          — FastMCP instance, config, engines, constants
- typer_responses.py    — response envelope helpers
- _server_helpers.py  — all private helper functions
- mcp_resources.py    — @mcp.resource handlers
- mcp_tools_validation.py — validate_file, validate_for_import, check_specific,
                              get_validation_summary, suggest_fixes
- mcp_tools_fix.py    — autofix_file, generate_skeleton, extract_methods_to_xml
- mcp_tools_batch.py  — validate_batch, autofix_batch
- mcp_tools_orchestration.py — process_twincat_single, process_twincat_batch,
                                verify_determinism_batch,
                                get_effective_oop_policy, lint_oop_policy

This facade re-registers all tools/resources by calling the register_*()
functions, then re-exports all public names so that:
  from twincat_validator.server import autofix_file
  from server import autofix_file
both continue to work.

MCP Tools:
- validate_file, autofix_file, validate_batch, autofix_batch
- process_twincat_single, process_twincat_batch, verify_determinism_batch
- get_effective_oop_policy, lint_oop_policy
- check_specific, validate_for_import, get_validation_summary
- suggest_fixes, generate_skeleton, extract_methods_to_xml
- get_effective_oop_policy
- lint_oop_policy

MCP Resources:
- validation-rules://, fix-capabilities://, naming-conventions://
- config://server-info, knowledge-base://, knowledge-base://checks/{check_id}
- knowledge-base://fixes/{fix_id}, generation-contract://
- generation-contract://types/{file_type}
- oop-policy://defaults, oop-policy://effective/{target_path}

Author: Jaime Calvente Mieres
License: MIT
Version: 1.0.0
"""

# ============================================================================
# SHARED STATE / CONSTANTS — re-exported for backward compatibility
# ============================================================================

from twincat_validator.typer_configuration import (  # noqa: F401
    config,
    app
)





# ============================================================================
# SERVER STARTUP
# ============================================================================


def main():
    """Entry point for console script and python -m invocation."""
    import logging

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)
    logger.info(f"Starting {config.server_info['name']} v{config.server_info['version']}")
    logger.info(f"Supported file types: {', '.join(config.server_info['supported_file_types'])}")
    logger.info(f"Validation checks: {config.server_info['validation_checks']}")
    logger.info(f"Auto-fix capabilities: {config.server_info['auto_fix_capabilities']}")
    logger.info("Server ready to accept connections")

    app()

if __name__ == "__main__":
    main()
