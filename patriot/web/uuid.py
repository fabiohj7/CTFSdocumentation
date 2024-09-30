import hashlib
import os
import uuid

from flask import (Flask, abort, jsonify, redirect, render_template, request,
                   session)

secure_key = hashlib.sha256(
    f'secret_key_{server_start_str}'.encode()).hexdigest()
app.secret_key = secure_key
