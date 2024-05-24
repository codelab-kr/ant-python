# 개미 수열

## 설명

- 개미 수열을 구현하기 위해 브루트 포스와 메모이제이션 방법을 사용하였습니다.
- 메모이제이션의 시간복잡도는 O(n), 공간복잡도는 O(n)이고 \
  브루트 포스의 시간복잡도는 O(2^n), 공간복잡도는 O(1)입니다.
- 메모이제이션을 사용하면 중복되는 계산을 피할 수 있어 시간복잡도가 줄어듭니다.

<br>

## 사전 요구사항

- 시스템에 Python 3.6 이상이 설치되어 있어야 합니다.
- 필요한 Python 패키지: [pytest]

<br>

## 설치

1. 저장소를 clone 합니다.

    ```
    git clone https://github.com/codelab-kr/ant-python.git
    cd ant-python
    ```

2. 가상환경을 생성하고 활성화합니다.

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. 다음 명령을 실행하여 필요한 Python 패키지를 설치합니다.

    ```
    pip3 install pytest
    ```

<br>

## 사용 및 테스트

1. 다음 명령을 사용하여 스크립트를 실행하면 결과(m)를 확인할 수 있습니다.

    ```shell
    # <n>은 3 초과, 100 미만의 양의 정수
    python -m brute_force.main <n>
    python -m memoization.main <n>
    ```

2. 다음 명령을 사용하여 테스트를 실행합니다.

    ```
    pytest
    ```
