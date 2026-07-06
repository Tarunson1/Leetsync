"""
Central logging configuration for LeetSync.
"""

import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Args:
        name: Logger name.

    Returns:
        Configured logger instance.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )

    return logging.getLogger(name)