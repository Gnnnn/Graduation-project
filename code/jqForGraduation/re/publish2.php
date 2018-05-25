<?php  
 session_start();
$request=$_GET["request"];

$GLOBALS['dbip'] = '18.218.245.165';
$GLOBALS['usn'] = 'root';
$GLOBALS['psw'] = 'test';
$GLOBALS['dbname'] = 'Gra';


if($request=="uploadfile"){
  $filetag = "";
  $fileName = "";
  $fileUrl = "";
  $dbtag = "";
  $filetag = $_POST["usertag"];
  // echo var_dump($filetag);
  // $allowedExts = array("gif", "jpeg", "jpg", "png","doc","txt","docx","elxs","els");
    $temp = explode(".", $_FILES["file"]["name"]);
    $extension = end($temp);     // 获取文件后缀名
    // echo $_FILES["file"]["type"]."  ".$_FILES["file"]["size"];
    // if ((($_FILES["file"]["type"] == "image/gif")
    // || ($_FILES["file"]["type"] == "image/jpeg")
    // || ($_FILES["file"]["type"] == "image/jpg")
    // || ($_FILES["file"]["type"] == "image/pjpeg")
    // || ($_FILES["file"]["type"] == "image/x-png")
    // || ($_FILES["file"]["type"] == "image/png"))
    // && ($_FILES["file"]["size"] < 2048000)   
    // && in_array($extension, $allowedExts))
    // {
    //   if ($_FILES["file"]["error"] > 0)
    //   {
    //       $fileUrl = null;
    //     echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    //   }
    //   else
    //   {
    //     if (file_exists("../upload/" . $_FILES["file"]["name"]))
    //     {
    //       $fileUrl = "upload/" . $_FILES["file"]["name"];
    //     }
    //     else
    //     {
    //       move_uploaded_file($_FILES["file"]["tmp_name"], "../upload/" . $_FILES["file"]["name"]);
    //       $fileUrl = "upload/" . $_FILES["file"]["name"];
    //     }
    //   }
    // }
    // else{
    //   $fileUrl = null;
    // }

  if (file_exists("../uploadFileFolder/" . $_FILES["file"]["name"]))
  {
    $fileUrl = "uploadFileFolder/" . $_FILES["file"]["name"];
  }
  else
  {
    move_uploaded_file($_FILES["file"]["tmp_name"], "../uploadFileFolder/" . $_FILES["file"]["name"]);
    $fileUrl = "uploadFileFolder/" . $_FILES["file"]["name"];
  }
  $fileName = $_FILES["file"]["name"];
  
  $dbtag = $_POST["inst"];
  $uploadTime = date('Y-m-d H:i:s');
  $con = new mysqli($dbip,$usn,$psw,$dbname);
  mysqli_query($con,"SET NAMES 'UTF8'");
  $sql = "INSERT INTO file(fileTag,fileName,filePath,toDB,uploadTime) VALUES ('{$filetag}','{$fileName}','{$fileUrl}','{$dbtag}','{$uploadTime}');";
  echo $sql;
  $result = mysqli_query($con,$sql);
  $result = mysqli_query($con,"SELECT fileUrl from file where fileUrl = '{$fileUrl}';");
  if(!mysqli_num_rows($result)){
    echo json_encode(array("isUpdate"=>0));
  } 
  else{
    echo "<script>alert('发布成功！'); </script>";
    echo json_encode(array("isUpdate"=>1));
    // header("Location: ../myinfor.html"); 
  }
  // echo var_dump($dbtag);
  if($dbtag == 'MySQL'){
    $shell = "python ../python/exceltomysql.py ../{$fileUrl}";
    echo $shell;
    $a = shell_exec($shell);
    echo $a;
    echo "<script>alert('存储成功！');history.go(-1); </script>";
    return ;
  }
  else if($dbtag == 'neo4j'){
    
    return ;
  }
  else if($dbtag == 'db4o'){
    return ;
  }
  else if($dbtag == 'MongoDB'){
    echo "<script>history.go(-1); </script>";
    return ;
  }
  else if($dbtag == 'No'){
    echo "<script>alert('暂不存储！');history.go(-1); </script>";
    return ;
  }
}
?>