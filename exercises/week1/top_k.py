from typing import List, Dict

def top_k_predictions(predictions:List[Dict],k: int)->List[Dict]:
    """
    Return the k top predictions
    Args:
        predictions: list of dictionaries with keys: "lable" and "score"
        k: number of top predictions
    Returns:
        list of top k predictions dictionaries
    Raises:
        ValueError: If k is negative
        KeyError: If required keys are missing. 
    """
    if k<0:
        raise ValueError('K value cannot be negative')
    for  pred in predictions:
        if "score" not in pred:
            raise KeyError("Each prediction should contain a 'score' key")
    sorted_preds = sorted(predictions,key=lambda x:x['score'],reverse=True)
    return sorted_preds[:k]