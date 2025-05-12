def check_if_available(reason:  str) -> str:
    """
    Checa o status de lançamento do jogo.

    Args:
        reason (str): tags de estado do jogo na página steam.

    Returns:
        status (str): Status de lançamento do jogo.
    """

    if reason.startswith('Now Available'):
        return 'Full Release'
    elif reason.startswith('Early Access'):
        return 'Early Access'
    elif reason.startswith('Pre-Purchase'):
        return 'Pre-Order'