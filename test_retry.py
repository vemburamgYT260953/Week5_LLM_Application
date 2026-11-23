from app.services.retry_service import retry_llm_call


attempts = 0


@retry_llm_call
def simulate_llm_failure():
    global attempts
    attempts += 1

    print(f"Attempt: {attempts}")

    if attempts < 3:
        raise ValueError("Simulated temporary failure")

    return "LLM response successful"


def test_retry_success():
    global attempts
    attempts = 0

    result = simulate_llm_failure()

    assert result == "LLM response successful"
    assert attempts == 3

@retry_llm_call
def always_fail():
    global attempts
    attempts += 1

    raise ValueError("Permanent failure")


def test_retry_maximum_attempts():
    global attempts
    attempts = 0

    try:
        always_fail()
        assert False, "Expected ValueError"
    except ValueError:
        pass

    assert attempts == 3

