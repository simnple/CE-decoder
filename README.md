# CE DECODE TOOL

Cheat Engine의 **decodeFunction**의 기능을 대신하여 LuaS로 컴파일링 시켜줍니다.

아래 사이트를 참고하였습니다.

https://github.com/cheat-engine/cheat-engine/blob/184e2553a8950772ea54d72c780820fbb7b712bd/Cheat%20Engine/LuaHandler.pas#L11983

## 사용법

해당 파일을 실행하기 전 인코딩된 코드가 필요합니다.

만약 얻지 못한 경우에는 CEtrainer.decrypter.jar 을 사용하시기 바랍니다.

```
py Main.py
```

바이트코드를 얻었다면, unluac로 디컴파일을 진행하거나 원하는대로 조리하면 됩니다.

## 디코딩의 작동 원리

1. decodeFunction을 통해 인자를 받습니다.
2. 치트 엔진 자체의 base85 디코딩을 거쳐 바이너리로 변환됩니다. 
3. 디코딩된 바이너리를 zlib을 이용하여 압축을 풉니다.
4. 압축을 풀어서 나온 바이트코드를 로드합니다.