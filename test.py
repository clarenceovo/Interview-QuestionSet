from app import main_function
from util.test_base import set_keyboard_input,get_display_output
import json

def test_create_canvas():
    global test_result
    global test_input
    test_input = json.load(open("testcase/test_input.json"))
    test_result = json.load(open("testcase/test_result.json"))
    set_keyboard_input(test_input['test_create_canvas'])
    main_function()
    output = get_display_output()
    assert output[2]== test_result['test_create_canvas'][0]

def test_create_canvas_add_lines():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_lines'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_add_lines'][0] #for c 30 30
    assert output[4] == test_result['test_create_canvas_add_lines'][1] #for L 1 2 6 2
    assert output[6] == test_result['test_create_canvas_add_lines'][2] #for L 6 3 6 4

def test_create_canvas_add_rectangle():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_rectangle'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_add_rectangle'][0]
    assert output[4] == test_result['test_create_canvas_add_rectangle'][1]
    assert output[6] == test_result['test_create_canvas_add_rectangle'][2]

def test_create_canvas_add_rectangle_and_outer_fill():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_rectangle_and_outer_fill'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_add_rectangle_and_outer_fill'][0]
    assert output[4] == test_result['test_create_canvas_add_rectangle_and_outer_fill'][1]
    assert output[6] == test_result['test_create_canvas_add_rectangle_and_outer_fill'][2]


def test_create_canvas_add_rectangle_and_inner_fill():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_rectangle_and_inner_fill'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_add_rectangle_and_inner_fill'][0]
    assert output[4] == test_result['test_create_canvas_add_rectangle_and_inner_fill'][1]
    assert output[6] == test_result['test_create_canvas_add_rectangle_and_inner_fill'][2]

def test_create_canvas_out_of_range_line():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_out_of_range_line'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_out_of_range_line'][0]
    assert output[4] == test_result['test_create_canvas_out_of_range_line'][1]

def test_create_canvas_out_of_range_rectangle():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_out_of_range_rectangle'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_out_of_range_rectangle'][0]
    assert output[4] == test_result['test_create_canvas_out_of_range_rectangle'][1]


def test_create_canvas_out_of_range_backfill():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_out_of_range_backfill'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_out_of_range_backfill'][0]
    assert output[4] == test_result['test_create_canvas_out_of_range_backfill'][1]

def test_create_canvas_out_of_range_line_at_zero():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_out_of_range_line_at_zero'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_out_of_range_line_at_zero'][0]
    assert output[4] == test_result['test_create_canvas_out_of_range_line_at_zero'][1]

def test_create_canvas_out_of_range_line_at_negative():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_out_of_range_line_at_negative'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_out_of_range_line_at_negative'][0]
    assert output[4] == test_result['test_create_canvas_out_of_range_line_at_negative'][1]

def test_create_canvas_create_canva_wrong_input_type():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_create_canva_wrong_input_type'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_create_canva_wrong_input_type'][0]

def test_create_canvas_create_canva_missing_input():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_create_canva_missing_input'])
    main_function()
    output = get_display_output()
    assert output[2] == test_result['test_create_canvas_create_canva_missing_input'][0]

def test_create_canvas_add_line_wrong_input_type():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_line_wrong_input_type'])
    main_function()
    output = get_display_output()
    assert output[4] == test_result['test_create_canvas_add_line_wrong_input_type'][0]


def test_create_canvas_add_line_missing_input():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_line_missing_input'])
    main_function()
    output = get_display_output()
    assert output[4] == test_result['test_create_canvas_add_line_missing_input'][0]


def test_create_canvas_add_line_not_horizontal_nor_vertical_line_1():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_line_not_horizontal_nor_vertical_line_1'])
    main_function()
    output = get_display_output()
    assert output[4] == test_result['test_create_canvas_add_line_not_horizontal_nor_vertical_line_1'][0]

def test_create_canvas_add_line_not_horizontal_nor_vertical_line_2():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_line_not_horizontal_nor_vertical_line_2'])
    main_function()
    output = get_display_output()
    assert output[4] == test_result['test_create_canvas_add_line_not_horizontal_nor_vertical_line_2'][0]


def test_create_canvas_add_rectanlge_missing_input():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_rectanlge_missing_input'])
    main_function()
    output = get_display_output()
    assert output[4] == test_result['test_create_canvas_add_rectanlge_missing_input'][0]

def test_create_canvas_add_rectanlge_wrong_input_type():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_add_rectanlge_wrong_input_type'])
    main_function()
    output = get_display_output()
    assert output[4] == test_result['test_create_canvas_add_rectanlge_wrong_input_type'][0]


def test_create_canvas_fill_missing_input():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_fill_missing_input'])
    main_function()
    output = get_display_output()
    assert output[6] == test_result['test_create_canvas_fill_missing_input'][0]

def test_create_canvas_fill_wrong_input_type():
    global test_result
    global test_input
    set_keyboard_input(test_input['test_create_canvas_fill_wrong_input_type'])
    main_function()
    output = get_display_output()
    assert output[6] == test_result['test_create_canvas_fill_wrong_input_type'][0]