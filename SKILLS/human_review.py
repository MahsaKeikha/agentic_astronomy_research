def apply(x:dict,approved:bool=False)->dict:return {"output":x,"approved":approved,"requires_human_review":not approved}
