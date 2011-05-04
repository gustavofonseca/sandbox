<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html xmlns:tal="http://xml.zope.org/namespaces/tal">
    <body>        
        % if failed_attempt:
            <p><font color="red">Invalid credentials, try again.</font></p>
        % endif
        <form method="post" action="${ request.path }">
            <p>
                <label for="login">Login</label><br>
                <input type="text" name="login" value="${ login }">
            </p>
            <p>
                <label for="passwd">Password</label><br>
                <input type="password" name="passwd">
            </p>
            <input type="hidden" name="next" value="${ next }">
            <input type="submit" name="submit">
        </form>
    </body>    
</html>