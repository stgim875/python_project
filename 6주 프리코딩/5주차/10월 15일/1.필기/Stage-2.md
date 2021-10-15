### Stage-2 누가 먼저할지 순서정하기

사용자로부터 선공, 후공에 대한 정보를 입력받은 뒤 사용자의 차례와 컴퓨터의 차례를 구분하고, 사용자 차례 때의 시행을 제작합니다.

#### 코딩 시작하기!

사용자로부터 선후에 대한 정보를 0과 1을 통해 받도록 합니다. 약간의 수학적인 연산을 적용하여 순서를 구분합니다. 이어서 사용자의 차례 때
입력받은 숫자만큼 출력해주는 시행을 구현 합니다.

<선공, 후공을 입력받고 사용자의 호출까지>

### 순서 구분하기

#### 순서란 어떻게 될까?

순서에 대해서 코딩하기 위해서 이 과정을 수학적으로 접근해야 합니다. 수학과 코딩이 우리의 사고력을 길러준다는 말이 이런 뜻이 아닐까 싶네요!
서로가 호출을 시행한다는 것은 시행을 하면 할 수록 숫자가 커짐을 의미합니다. 그리고 그 수는 1씩 증가하죠. 그리고 증가하는 과정에서 특징이 있습니다.
홀수번과 짝수번으로 구분하여 시행하는 사람이 같다는 점이죠. 이를 그림으로 다시 이해해봅시다.

|      서비스명       |                               버전명                               |
| :-----------------: | :----------------------------------------------------------------: |
|     `dashboard`     |     repo.iris.tools/iris/dashboard:v3.0.1-RC20210830.0-077f460     |
|      `cluster`      |      repo.iris.tools/iris/cluster:v3.0.1-RC20210830.0-3a1ebf0      |
|    `db-browser`     |    repo.iris.tools/iris/db-browser:v3.0.1-RC20210830.0-8a1c911     |
|   `hdfs-browser`    |   repo.iris.tools/iris/hdfs-browser:v3.0.1-RC20210830.0-36ae81f    |
|       `jhms`        |             repo.iris.tools/iris/jhms:3.0.2.1_44100f8              |
|       `meta`        |       repo.iris.tools/iris/meta:v3.0.1-RC20210908.0-61de888        |
|      `sherman`      |      repo.iris.tools/iris/sherman:v3.0.1-RC20210908.0-d8d7b7f      |
|      `studio`       |      repo.iris.tools/iris/studio:v3.0.1-RC20210913.0-742e9a7       |
|   `map-analyzer`    | repo.iris.tools/iris/iris-map-analyzer:v3.0.1-RC20210913.0-df82905 |
|      `angora`       |      repo.iris.tools/iris/angora:v3.0.1-RC20210914.0-4225633       |
| `iris-web-platform` | repo.iris.tools/iris/iris-web-platform:v3.0.1-RC20210915.0-a63887c |
