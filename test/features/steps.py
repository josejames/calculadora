# -*- coding: utf-8 -*-
from lettuce import *
import sys
sys.path.append('../')
from Calculator import Calculator


@step(u'Given I have the number "([^"]*)" and the number "([^"]*)"')
def given_i_have_the_number_group1_and_the_number_group2(step, number1, number2):
    world.number1 = number1
    world.number2 = number2

@step(u'When I add them')
def when_i_add_them(step):
	cal = Calculator()
	world.resultado = cal.suma(int(world.number1),int(world.number2))

@step(u'When I substrac them')
def when_i_substrac_them(step):
    cal = Calculator()
    world.resultado = cal.resta(int(world.number1),int(world.number2))

@step(u'When I multiply them')
def when_i_multiply_them(step):
    cal = Calculator()
    world.resultado = cal.multiplicacion(int(world.number1),int(world.number2))
    
@step(u'Then I see the number "([^"]*)"')
def then_i_see_the_number_group1(step, expected):
    assert world.resultado == int(expected), "resultado {0}, esperado {1}".format(world.resultado,expected) 
