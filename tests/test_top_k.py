#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 29 16:22:32 2026

@author: fkaka
"""

import pytest
from exercises.week1.top_k import top_k_predictions


def test_basic_top_k():
    # correct prediction
    preds = [
        {"label": "a", "score": 0.5},
        {"label": "b", "score": 0.9},
        {"label": "c", "score": 0.7},
    ]

    result = top_k_predictions(preds, 2)

    assert len(result) == 2
    assert result[0]["label"] == "b"
    assert result[1]["label"] == "c"


def test_k_greater_than_length():
    # only one prediction
    preds = [{"label": "a", "score": 0.5}]
    result = top_k_predictions(preds, 5)

    assert len(result) == 1


def test_k_zero():
    # k = 0 should come back without 
    preds = [{"label": "a", "score": 0.5}]
    result = top_k_predictions(preds, 0)

    assert result == []


def test_empty_list():
    # k more than length of predictions 
    result = top_k_predictions([], 3)
    assert result == []


def test_negative_k():
    # check negative k values
    with pytest.raises(ValueError):
        top_k_predictions([], -1)


def test_missing_score_key():
    # No score values 
    preds = [{"label": "a"}]
    with pytest.raises(KeyError):
        top_k_predictions(preds, 1)
