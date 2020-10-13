from my_proj import thank, complain, complete_task, assign_task, pay

def test_thank():
    assert thank() == True

def test_complain():
    assert complain() == True

def test_complete_task():
    assert complete_task() == True

def test_assign_task():
    assert assign_task() == True

def test_pay():
    assert pay() == True
