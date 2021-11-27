package hello.core.member;


/*
회원 서비스 : 1. 회원가입 2.회원조회
 */
public interface MemberService {

    // 1. 회원 가입
    void join(Member member);

    // 2. 회원 조회
    Member findMember(Long memberId);
}
