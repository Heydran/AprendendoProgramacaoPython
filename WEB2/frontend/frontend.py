from flask import Flask, render_template, request, redirect, session
import peewee_site as p

app = Flask("__name__")
app.secret_key = 'senha'

