<?php  
 session_start();
$request=$_GET["request"];

$GLOBALS['dbip'] = '****';
$GLOBALS['usn'] = '****';
$GLOBALS['psw'] = '****';
$GLOBALS['dbname'] = 'xcxcketest_com';

if($request=="viewmyinfo"){
  $username=$_SESSION["username"];
  if(!$username){
    echo json_encode(array("isLogin"=>0));  
    }
  else{
      $con = new mysqli($dbip,$usn,$psw,$dbname);
      mysqli_query($con,"SET NAMES 'UTF8'");
      $result=mysqli_query($con,"SELECT usertel,usermail,usergender,usertag,userpic from user where username = '{$username}';");
      $row1 = mysqli_fetch_array($result);
      echo json_encode(array("usertel"=>$row1[usertel],"usermail"=>$row1[usermail],"usergender"=>$row1[usergender],"usertag"=>$row1[usertag],"userpic"=>$row1[userpic],"username"=>$username));
        return;
        }
}


if($request=="myinfo"){
    $usertag = $_POST["usertag"];
    //file start
    $allowedExts = array("gif", "jpeg", "jpg", "png");
    echo $_FILES["file"]["name"];
      $temp = explode(".", $_FILES["file"]["name"]);
      $extension = end($temp);     // 获取文件后缀名
      // echo $_FILES["file"]["type"]."  ".$_FILES["file"]["size"];
      if ((($_FILES["file"]["type"] == "image/gif")
      || ($_FILES["file"]["type"] == "image/jpeg")
      || ($_FILES["file"]["type"] == "image/jpg")
      || ($_FILES["file"]["type"] == "image/pjpeg")
      || ($_FILES["file"]["type"] == "image/x-png")
      || ($_FILES["file"]["type"] == "image/png"))
      && ($_FILES["file"]["size"] < 2048000)   
      && in_array($extension, $allowedExts))
      {
        if ($_FILES["file"]["error"] > 0)
        {
            $picurl = null;
          echo "错误：: " . $_FILES["file"]["error"] . "<br>";
        }
        else
        {
          if (file_exists("../upload/" . $_FILES["file"]["name"]))
          {
            $picurl = "upload/" . $_FILES["file"]["name"];
          }
          else
          {
            move_uploaded_file($_FILES["file"]["tmp_name"], "../upload/" . $_FILES["file"]["name"]);
            $picurl = "upload/" . $_FILES["file"]["name"];
          }
        }
      }
      else{
        $picurl = null;
      }
    //file end

    // fileFolder start
    if (file_exists("../uploadFileFolder/" . $_FILES["file"]["name"]))
    {
      $picurl = "uploadFileFolder/" . $_FILES["file"]["name"];
    }
    else
    {
      move_uploaded_file($_FILES["file"]["tmp_name"], "../uploadFileFolder/" . $_FILES["file"]["name"]);
      $picurl = "uploadFileFolder/" . $_FILES["file"]["name"];
    }
    // fileFolder end

    $con = new mysqli($dbip,$usn,$psw,$dbname);
    mysqli_query($con,"SET NAMES 'UTF8'");
    //bug start 
    $result1 = mysqli_query($con,"SELECT usertag from user where username = '{$username}';"); 
    $row1 = mysqli_fetch_array($result1);
    $old_usertag = $row1[usertag];
    if($usertag == null){
      $usertag = $old_usertag;
    }
    $result = mysqli_query($con,"UPDATE user SET `usertag`= '{$usertag}';");
    $result = mysqli_query($con,"SELECT username from user where usertag = '{$usertag}';");
    if(!mysqli_num_rows($result)){
    echo json_encode(array("isUpdate"=>0));
    return;
    } 
    else{
    // echo "<script>alert('发布成功！'); history.go(-1);</script>";
    header("Location: ../myinfor.html"); 
    //确保重定向后，后续代码不会被执行 
    return;
    }
  }
?>