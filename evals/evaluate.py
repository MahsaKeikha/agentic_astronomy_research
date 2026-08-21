def evaluate(result):
    required = {"input", "stages", "status"}
    return {"passed": required.issubset(result), "stage_count": len(result.get("stages", []))}
