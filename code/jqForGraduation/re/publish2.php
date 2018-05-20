<?php  
 session_start();
$request=$_GET["request"];

$GLOBALS['dbip'] = '18.218.245.165';
$GLOBALS['usn'] = 'root';
$GLOBALS['psw'] = 'test';
$GLOBALS['dbname'] = 'Gra';


if($request=="dbstore"){

}


if($request=="uploadfile"){
  $filetag = $_POST["usertag"];
  $fileName = $_FILES["file"]["name"];
  $fileUrl = "uploadFileFolder/" . $_FILES["file"]["name"];
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

  // fileFolder start
  move_uploaded_file($_FILES["file"]["tmp_name"], "../uploadFileFolder/" . $_FILES["file"]["name"]);
  // fileFolder end
  $dbtags = $_POST["inst"];
  $dbtag = implode(',',$dbtags);
  $con = new mysqli($dbip,$usn,$psw,$dbname);
  mysqli_query($con,"SET NAMES 'UTF8'");
  $uploadTime = date('Y-m-d H:i:s');
  $sql = "INSERT INTO file set fileName = '{$fileName}',fileTag = '{$filetag}',filePath = '{$fileUrl}',uploadTime='{$uploadTime}',toDB='{$dbtag}';";
  echo $sql;
  $result = mysqli_query($con,$sql);
  $result = mysqli_query($con,"SELECT filePath from file where filePath = '{$fileUrl}';");
  if(!mysqli_num_rows($result)){
    echo "<script>alert('发布失败！'); </script>";
    echo json_encode(array("isUpdate"=>0));
  } 
  else{
    echo "<script>alert('发布成功！'); </script>";
    echo json_encode(array("isUpdate"=>1));
    //确保重定向后，后续代码不会被执行 
  }
  $dbrags = $_POST["inst"];
  $dbtag = implode(',',$dbrags);
  echo $dbtag;
  if($dbtag == 'MySQL'){
    $sys = "python ../python/exceltomysql.py "+$fileUrl+''+'方便面属性';
    echo $sys;
    $a = shell_exec($sys);
    echo $a;
    echo "<script>alert('存储成功！'); history.go(-1);</script>";
    return ;

  }
  else if($dbtag == 'neo4j'){
    return ;
  }
  else if($dbtag == 'db4o'){
    return ;
  }
  else if($dbtag == 'MongoDB'){
    return ;
  }
  else if($dbtag == 'No'){
    return ;
  }
}
?>