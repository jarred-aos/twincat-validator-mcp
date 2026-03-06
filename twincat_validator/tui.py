#!/usr/bin/env python3
"""
TwinCAT Validator MCP Server — thin facade.

The real implementation lives in the sub-modules:
- mcp_app.py          — FastMCP instance, config, engines, constants
- mcp_responses.py    — response envelope helpers
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

TUI Tools:
- validate_file, autofix_file, validate_batch, autofix_batch
- process_twincat_single, process_twincat_batch, verify_determinism_batch
- get_effective_oop_policy, lint_oop_policy
- check_specific, validate_for_import, get_validation_summary
- suggest_fixes, generate_skeleton, extract_methods_to_xml
- get_effective_oop_policy
- lint_oop_policy

Author: Jaime Calvente Mieres
License: MIT
Version: 1.0.0
"""
import json

# ============================================================================
# REGISTER ALL RESOURCES AND TOOLS
# ============================================================================

from twincat_validator.tui_tools_validation import validate_file
from twincat_validator.tui_tools_fix import autofix_file
# from twincat_validator.mcp_tools_batch import register_batch_tools
# from twincat_validator.mcp_tools_orchestration import register_orchestration_tools


# ============================================================================
# SERVER STARTUP
# ============================================================================


def main():
    """Entry point for console script and python -m invocation."""
    import logging

    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    logger = logging.getLogger(__name__)

    input_filepath = r"C:\Users\jarredb\Documents\PLC\twincat-aw5_testing\Twincat_AW5\AW5\01_WeldingAxes\Motion_Functions\FB_THREE_AXIS_ABSOLUTE_MOVE.TcPOU"

    logger.info("Starting file validation")
    response = validate_file(input_filepath)
    response = json.loads(response)
    logger.info(json.dumps(response['issues'], indent=2))
    logger.info("Starting file autofix")
    response = autofix_file(input_filepath)
    
    logger.info(response)
    logger.info("Completed file validation")
    # mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
