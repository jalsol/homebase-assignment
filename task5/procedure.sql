DELIMITER //
CREATE PROCEDURE AddPost(IN p_title VARCHAR(255), IN p_content TEXT)
BEGIN
    INSERT INTO post (title, content)
    VALUES (p_title, p_content);
END //

CREATE PROCEDURE GetPost(IN p_id BIGINT)
BEGIN
    SELECT * FROM post
    WHERE id = p_id;
END //

CREATE PROCEDURE UpdatePost(IN p_id BIGINT, IN p_title VARCHAR(255), IN p_content TEXT)
BEGIN
    UPDATE post
    SET title = p_title, content = p_content
    WHERE id = p_id;
END //

CREATE PROCEDURE DeletePost(IN p_id BIGINT)
BEGIN
    DELETE FROM post
    WHERE id = p_id;
END //

CREATE PROCEDURE AddComment(IN p_id BIGINT, IN p_comment TEXT)
BEGIN
    INSERT INTO comment (post_id, comment)
    VALUES (p_id, p_comment);
END //

CREATE PROCEDURE GetCommentsForPost(IN p_id BIGINT)
BEGIN
    SELECT * FROM comment
    WHERE post_id = p_id;
END //

CREATE PROCEDURE DeleteComment(IN c_id BIGINT)
BEGIN
    DELETE FROM comment
    WHERE id = c_id;
END //

CREATE PROCEDURE GetAllPostsAndComments()
BEGIN
    SELECT p.*, c.id, c.comment
    FROM post p LEFT JOIN comment c
    ON p.id = c.post_id;
END //
DELIMITER ;