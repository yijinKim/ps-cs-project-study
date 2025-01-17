[TOC]

------

# OSI 7 Layer

<br>

## Application Layer

- OSI 7 Layer의 Session Layer(L5), Presentation Layer(L6), Application layer(L7)이 TCP/IP모델에서는 Application Layer로 통합되었다.
- TCP/IP Updated 모델에서도 해당 계층은 유지된다.
- 클라이언트 서버로 이루어진 애플리케이션에서 통신하기 위해 사용한다.
- TCP/IP 소켓 프로그래밍(Transport layer에서 제공하는 API를 활용해 통신 가능한 프로그램 만드는 것)
  - Application Layer 프로토콜(인코더, 디코더)을 만들어서 사용 가능하다.
- 대표적 프로토콜
  -  **HTTP (Hyper-Text Transfer Protocol)** : TCP기반의 프로토콜로 포트번호 80번을 사용합니다.
  - **Telnet** : TCP 포트번호 23번을 사용합니다. 원격 터미널을 접속할때 이 포로토콜을 사용합니다.
  - **SSH (Secure Shell)** : 텔넷과 같은 서비스는 보안에 취약합니다. 비밀번호가 암호화되지 않아 그대로 노출이 되기 때문이지요. 이것을 보완한것이 SSH입니다. 포트번호 22번을 사용합니다.
  - **FTP(File Transfer Protocol)** : 파일 전송 프로토콜입니다. 파일을 받거나 올릴때 FTP를 사용하지요. FTP는 파일을 올리거나 내려받을때 신뢰성을 중요시하기 때문에 TCP에서 동작하구요. 2개의 포트를 사용합니다. TCP 포트 20번은 데이터 전송을 위한 용도, TCP 포트 21번은 제어용으로 사용합니다.
  - **SMTP (Simple Mail Transfer Protocol)** : 메일 전송 프로토콜입니다. TCP 상에서 동작하며 포트는 25번을 사용합니다.
  - **POP3 (Post Office Protocol Version3)** : 메일 수신용 프로토콜입니다. 아웃룩같은 프로그램이 POP3라는 프로토콜을 사용하여 동작합니다. TCP 포트 110번을 사용합니다.
  - **DNS (Domain Name System)** : 도메인명에 대한 호스트 정보를 제공해줍니다. 기본적으로 UDP상에서 동작합니다. 기본적으로 실패하면 다시 한번 요청하면 되며 그렇게 중요한 정보가 아니기 때문이죠. 하지만 신뢰성을 요할 경우에는 TCP상에서도 동작합니다. 데이터의 길이가 길 경우같은 때 TCP 기반으로 동작할 수 있습니다. UDP, TCP 포트 53번을 사용합니다.

- 사용자 인터페이스 제공하는 프로그램
- Data/Message 단위
- client-server 구조
- p2p 구조
- keep-alive 

<br>

## Transport Layer

1. 출발지부터 도착지까지 패킷이 제대로 전송될 수 있도록 한다.

2. 응용 계층에서 만든 데이터를 일정한 크기로 자른다.

   <br>

- 서로 다른 호스트에서 돌아가는 응용 프로세스 간 logical communication을 제공한다.
- 전송 프로토콜(Transport Protocol)은 종단점(end-system)에서 적용된다.
  - 송신 호스트 : 데이터 메시지를 세그먼트로 분해하여 네트워크 계층(3계층)으로 전송한다.
  - 수신 호스트 : 세그먼트들을 데이터 메시지로 재조립하여 응용 계층으로 전송한다.

- 전송 단위 : 세그먼트
- os커널에 소프트웨어적으로 구현

- 대표적인 프로토콜 

  - **TCP** 

    - Reliable, in-order delivery : 신뢰성 있게, 순서대로 전송한다.
    - Connection Setup : 데이터를 보내기 전에 상대방의 상태를 확인하고 보낸다.
    - Congestion control : 네트워크 상에서 패킷들이 몰려 발생하는 혼잡을 피하기 위해 보내는 패킷 양을 조절
    - Flow control : 라우터와 받는 수신자의 상황을 봐서 보내는 패킷 양을 조절
    - Delay나 Bandwidth를 건드리지는 못한다.

  - **UDP** 

    - Unreliable, unordered delivery
    - 꼭 필요한 기능만 전송하고 오류 제어 같은 추가 기능 필요로 하지 않는 애플리케이션에 사용된다.
    - 패킷을 어떤 수신자의 어떤 서비스가 받아야 하는지(IP주소, Port 번호), 패킷이 중간에 망가지지는 않았는지만 처리한다.
    - 나머지 기능은 제공 X

    

<br>

#### Multiplexing & Demultiplexing

- **네트워크 소켓 (Network Socket)** : 컴퓨터 네트워크의 사이에 있는 프로세스 간 통신의 종착점이다. 컴퓨터 간 통신의 대부분은 IP(인터넷 프로토콜)을 기반으로 하고 있고, 네트워크 소켓의 대부분은 인터넷 소켓이다. 네트워크 통신을 위해서 송,수신측에서는 소켓을 생성하고, 이 소켓을 통해 서로 데이터를 교환한다.

- **Multiplexing(다중화)** at Sender : 다수의 소켓들로부터 추가 정보(목적지 주소 등)를 얻어서 전송할 데이터의 헤더에 해당 정보(목적지 주소 등)를 추가하는 기능.
  
  - 여러 어플리케이션의 Socket들로부터 들어오는 데이터를 수집하여, 패킷으로 만들어 하위 레이어로 전송하는 것
  
- **Demultiplexing(역다중화)** at Receiver : 수신된 데이터를 적절한 소켓으로 전달하기 위해 헤더 정보를 이용한다. 하위 계층에서 상위 계층으로 올라갈 때마다 헤더가 작아지면서 전송할 데이터가 목적지에 도착한다.

  - 하위 레이어로부터 수신된 패킷을 올바른 Socket으로 전송하여 올바른 어플리케이션에게 전송하는 것.

    이때 정확한 어플리케이션의 Socket으로 전달해주기 위해 포트넘버를 활용한다.

  - 호스트는 IP 데이터그램(datagram)을 수신한다.

    - 각각의 데이터그램 출발지 IP주소, 목적지 IP주소를 가지고 있다.
    - 각각의 데이터그램은 하나의 전송계층 세그먼트를 옮긴다.
    - 각각의 세그먼트는 출발지, 목적지 포트번호(16bits)를 가지고 있다.

  - 비연결형 통신, UDP의 소켓

    - 생성된 소켓은 호스트 로컬 포트 번호(source port #)만 가지고 있다.
    - 호스트가 UDP 세그먼트를 받으면, 세그먼트에 있는 목적지 포트 번호를 확인한다.
    - 해당 포트 번호로 세그먼트를 안내한다.
    - 만약 서로 다른 출발지 IP주소, 포트 번호이지만 같은 목적지 포트번호나 IP주소를 가진 IP datagram을 받으면 목적지에서 같은 소켓으로 데이터가 전송된다.

  - 연결 지향형 통신, TCP의 소켓

    - 출발지 IP주소, 포트번호와 목적지 IP주소, 포트번호의 네 가지 요소로 소켓이 생성되어진다.
    - 수신자는 세그먼트를 적절한 소켓으로 안내하기 위해 네 가지 값 모두 이용한다.
    - 송신 호스트는 동시에 많은 TCP 소켓들을 지원할 수 있다. 단 각각의 소켓들은 각자 네 가지 요소를 가진며, 이를 통해 소켓이 구분된다.
    - 웹 서버(송신자)는 각각의 클라이언트를 연결하기 위해 다른 소켓들을 가진다.



<br>

## Network Layer

- Internet layer
- 네트워크 상에서의 패킷의 이동
- **서로 다른 네트워크 간의 통신을 가능하게 하는 역할**을 수행
- IP주소를 이용해 길을 찾고 다음 라우터에게 패킷을 넘겨주며 인터넷이 가능하게 만드는 계층
- 전송 단위 : 패킷
- **라우터** : 데이터의 목적지까지 어떤 경로로 가는게 좋은지 알려주는 기능
  - 라우팅 : 데이터 전송할 최적의 경로 찾는 행위
  - 라우팅 프로토콜 : 라우터 간 라우팅 정보 교환하기 위한 프로토콜.
    - ospf, 
  - 데이터를 전달하는것은 스위칭(데이터링크 계층)
- **IP**(Internet Protocol)
  - 캡슐화 할때, IP헤더(데이터를 다른 네트워크 목적지까지 보내기 위해 필요한 정보 보유함) 붙인다.
  - IP헤더 + 데이터(from Transport layer) = IP 패킷
  - IP주소 : 라우터가 목적지 식별하기 위해 사용하는 주소
  - IP프로토콜 버전
    - IPv4 : 32bit
    - IPv6 : 128bit
- subnet mask
- udp broadcast
- 비동기 동기
- tcp udp 차이







<br>

------

##### References

https://reakwon.tistory.com/68

https://movefast.tistory.com/24

https://velog.io/@kms9887/%EC%BB%B4%ED%93%A8%ED%84%B0-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-3.-Transport-Layer1

https://ddongwon.tistory.com/79

https://zion830.tistory.com/133?category=802372
