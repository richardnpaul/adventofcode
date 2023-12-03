#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def clean_line(line):
    stripped_line = line.strip()
    nogameline = stripped_line.replace('Game ', '')
    replace_semi_colon_line = nogameline.replace(';', ',')
    return replace_semi_colon_line


def create_games_dict(line, game_dict):
    game_no = line.split(':')[0]
    line = line.split(':')[1]
    line = line.split(',')
    game_dict = {}
    for item in line:
        item = item.split()
        colour = item[1]
        number = item[0]
        if colour in game_dict.keys():
            game_dict[colour] = max(int(game_dict.get(colour)), int(number))
        else:
            game_dict[colour] = int(number)
    return game_no, game_dict


def get_possible_games(game_dict):
    possible_games = []
    for game_no, game_dict in game_dict.items():
        if 'red' in game_dict:
            if game_dict['red'] > 12:
                continue
        if 'green' in game_dict:
            if game_dict['green'] > 13:
                continue
        if 'blue' in game_dict:
            if game_dict['blue'] > 14:
                continue
        possible_games.append(int(game_no))
    return possible_games

with open(sys.argv[1]) as f:
    lines = f.readlines()
    game_dict = {}
    possible_games = []
    for line in lines:
        cleaned_line = clean_line(line)
        game_no, game_no_dict = create_games_dict(cleaned_line, game_dict)
        game_dict[game_no] = game_no_dict
    print(f"Sum of possible games: {sum(get_possible_games(game_dict))}")
