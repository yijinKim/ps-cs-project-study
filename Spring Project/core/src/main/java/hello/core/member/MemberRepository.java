package hello.core.member;

public interface MemberRepository { // 회원 저장소

    // 회원 저장하는 기능
    void save(Member member);

    // 회원 id 찾는 기능
    Member findById(Long memberId);

}
