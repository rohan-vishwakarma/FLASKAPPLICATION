from flask import jsonify, request
from . import celery_bp
from celery import shared_task
from celery.result import AsyncResult


@celery_bp.route('/task')
def task():
    return "hello"

try:
    

    @celery_bp.post("/add")
    def start_add() -> dict[str, object]:
        a = request.form.get("a", type=int)
        b = request.form.get("b", type=int)
        result = add_together.delay(a, b)
        return jsonify({"result_id": result.id})
except Exception as e:
    print(e)
   
@celery_bp.get("/result/<id>")
def task_result(id: str) -> dict[str, object]:
    result = AsyncResult(id)
    return {
        "ready": result.ready(),
        "successful": result.successful(),
        "value": result.result if result.ready() else None,
    }


try:
    @shared_task(ignore_result=False)
    def add_together(a: int, b: int) -> int:
        return a + b

except Exception as e:
    print(e)

